package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.1 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A distinct article or unit within the digital domain.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Artifact extends Element {

  private Agent suppliedBy;
  private String builtTime;
  private List<Agent> originatedBy;
  private String releaseTime;
  private List<String> standardName;
  private List<String> supportLevel;
  private String validUntilTime;


}