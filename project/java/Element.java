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
  Base domain class from which all other SPDX-3.0 domain classes derive.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Element  {

  private URI type;
  private String comment;
  private CreationInfo creationInfo;
  private String description;
  private List<Extension> extension;
  private List<ExternalIdentifier> externalIdentifier;
  private List<ExternalRef> externalRef;
  private String name;
  private String summary;
  private List<IntegrityMethod> verifiedUsing;
  private URI spdxId;


}