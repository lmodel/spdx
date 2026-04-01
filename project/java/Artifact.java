package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  A distinct article or unit within the digital domain.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Artifact extends Element {

  private List<String> standardName;
  private ZonedDateTime builtTime;
  private ZonedDateTime validUntilTime;
  private List<String> supportLevel;
  private Agent suppliedBy;
  private List<Agent> originatedBy;
  private ZonedDateTime releaseTime;

}