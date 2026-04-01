package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Refers to any object that stores content on a computer.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class File extends SoftwareArtifact {

  private String fileKind;
  private String contentType;

}